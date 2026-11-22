# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 2:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1131 windows, 31255 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 598 | 34.4 | 35.2 | $-385.99 | -6.5% | $614.01 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3146 | 51.1 | 50.5 | $-840.97 | -2.7% | $159.03 | -1.5 | done | can't tell from luck |
| value_ev10 | 1464 | 38.0 | 39.2 | $-935.40 | -6.4% | $64.60 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2639 | 49.7 | 49.4 | $-1126.63 | -4.3% | $-126.63 | -2.2 | done | losing for real |
| value_ev5 | 2215 | 40.0 | 41.1 | $-1337.18 | -6.0% | $-337.18 | -2.4 | done | losing for real |
| trend_filter | 1851 | 49.1 | 50.4 | $-1426.67 | -7.7% | $-426.67 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2639 | 50.3 | 51.1 | $-1669.50 | -6.3% | $-669.50 | -3.3 | done | losing for real |
| coinflip | 4519 | 50.4 | 50.2 | $-1802.81 | -4.0% | $-802.81 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3146 | 48.9 | 50.2 | $-2096.12 | -6.7% | $-1096.12 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4519 | 50.3 | 51.4 | $-2732.02 | -6.0% | $-1732.02 | -4.2 | done | losing for real |
| always_up | 4519 | 47.7 | 49.4 | $-3505.69 | -7.8% | $-2505.69 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7165 | 48.3 | 49.0 | $-3722.72 |
| ETH | 7744 | 48.1 | 48.4 | $-4721.04 |
| SOL | 8137 | 48.0 | 48.4 | $-4650.94 |
| XRP | 8209 | 48.2 | 48.2 | $-4764.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
