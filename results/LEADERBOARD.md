# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 4:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1089 windows, 30118 settled trades, 70 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 566 | 34.8 | 35.2 | $-287.96 | -5.1% | $712.04 | -0.9 | done | can't tell from luck |
| value_ev10 | 1395 | 38.1 | 39.2 | $-848.24 | -6.1% | $151.76 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3044 | 51.1 | 50.5 | $-881.80 | -2.9% | $118.20 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2558 | 49.9 | 49.5 | $-1003.09 | -3.9% | $-3.09 | -2.0 | done | can't tell from luck |
| value_ev5 | 2121 | 40.0 | 41.1 | $-1211.11 | -5.7% | $-211.11 | -2.2 | done | losing for real |
| trend_filter | 1788 | 49.6 | 50.6 | $-1221.80 | -6.8% | $-221.80 | -3.0 | done | losing for real |
| coinflip | 4348 | 50.6 | 50.3 | $-1587.45 | -3.7% | $-587.45 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2558 | 50.1 | 51.1 | $-1726.50 | -6.7% | $-726.50 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 3044 | 48.9 | 50.3 | $-1982.27 | -6.5% | $-982.27 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4348 | 50.9 | 51.5 | $-2119.97 | -4.9% | $-1119.97 | -3.3 | done | losing for real |
| always_up | 4348 | 47.6 | 49.4 | $-3447.04 | -7.9% | $-2447.04 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6879 | 48.5 | 49.0 | $-3272.15 |
| ETH | 7462 | 48.2 | 48.5 | $-4322.65 |
| SOL | 7851 | 48.1 | 48.5 | $-4347.88 |
| XRP | 7926 | 48.3 | 48.3 | $-4374.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
