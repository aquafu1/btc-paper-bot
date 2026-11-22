# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 3:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1132 windows, 31265 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 599 | 34.4 | 35.2 | $-395.99 | -6.6% | $604.01 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3147 | 51.2 | 50.5 | $-835.65 | -2.7% | $164.35 | -1.5 | done | can't tell from luck |
| value_ev10 | 1465 | 38.0 | 39.2 | $-945.40 | -6.5% | $54.60 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2640 | 49.7 | 49.4 | $-1136.63 | -4.3% | $-136.63 | -2.2 | done | losing for real |
| value_ev5 | 2216 | 39.9 | 41.1 | $-1347.18 | -6.1% | $-347.18 | -2.4 | done | losing for real |
| trend_filter | 1851 | 49.1 | 50.4 | $-1426.67 | -7.7% | $-426.67 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2640 | 50.3 | 51.1 | $-1664.17 | -6.3% | $-664.17 | -3.3 | done | losing for real |
| coinflip | 4520 | 50.4 | 50.2 | $-1812.81 | -4.0% | $-812.81 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3147 | 48.8 | 50.2 | $-2106.12 | -6.7% | $-1106.12 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4520 | 50.3 | 51.4 | $-2726.70 | -6.0% | $-1726.70 | -4.2 | done | losing for real |
| always_up | 4520 | 47.7 | 49.4 | $-3500.36 | -7.7% | $-2500.36 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7165 | 48.3 | 49.0 | $-3722.72 |
| ETH | 7744 | 48.1 | 48.4 | $-4721.04 |
| SOL | 8137 | 48.0 | 48.4 | $-4650.94 |
| XRP | 8219 | 48.1 | 48.2 | $-4802.98 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
