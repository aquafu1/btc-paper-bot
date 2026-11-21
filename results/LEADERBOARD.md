# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 11:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1022 windows, 28451 settled trades, 68 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 525 | 34.7 | 35.1 | $-278.47 | -5.3% | $721.53 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2901 | 51.1 | 50.5 | $-848.49 | -2.9% | $151.51 | -1.6 | done | can't tell from luck |
| value_ev10 | 1302 | 37.5 | 39.2 | $-965.19 | -7.4% | $34.81 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2451 | 49.9 | 49.7 | $-1053.77 | -4.3% | $-53.77 | -2.1 | done | losing for real |
| trend_filter | 1703 | 49.7 | 50.8 | $-1184.18 | -7.0% | $-184.18 | -2.9 | done | losing for real |
| value_ev5 | 1977 | 39.4 | 41.0 | $-1404.73 | -7.1% | $-404.73 | -2.7 | done | losing for real |
| coinflip | 4080 | 50.5 | 50.4 | $-1640.00 | -4.0% | $-640.00 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2451 | 50.1 | 51.0 | $-1646.53 | -6.7% | $-646.53 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 2901 | 48.9 | 50.3 | $-1973.93 | -6.8% | $-973.93 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4080 | 50.8 | 51.5 | $-2179.96 | -5.3% | $-1179.96 | -3.5 | done | losing for real |
| always_up | 4080 | 47.4 | 49.5 | $-3560.75 | -8.7% | $-2560.75 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6486 | 48.3 | 49.1 | $-3509.11 |
| ETH | 7069 | 48.1 | 48.5 | $-4384.32 |
| SOL | 7432 | 48.2 | 48.6 | $-4191.81 |
| XRP | 7464 | 48.2 | 48.4 | $-4650.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
