# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 11:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1021 windows, 28425 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 525 | 34.7 | 35.1 | $-278.47 | -5.3% | $721.53 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2898 | 51.2 | 50.5 | $-818.49 | -2.8% | $181.51 | -1.5 | done | can't tell from luck |
| value_ev10 | 1301 | 37.5 | 39.2 | $-955.19 | -7.3% | $44.81 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2449 | 49.9 | 49.7 | $-1069.34 | -4.4% | $-69.34 | -2.2 | done | losing for real |
| trend_filter | 1703 | 49.7 | 50.8 | $-1184.18 | -7.0% | $-184.18 | -2.9 | done | losing for real |
| value_ev5 | 1974 | 39.5 | 41.0 | $-1374.73 | -7.0% | $-374.73 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2449 | 50.1 | 51.0 | $-1626.53 | -6.6% | $-626.53 | -3.4 | done | losing for real |
| coinflip | 4076 | 50.5 | 50.4 | $-1651.88 | -4.1% | $-651.88 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2898 | 48.8 | 50.3 | $-1996.10 | -6.9% | $-996.10 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4076 | 50.8 | 51.5 | $-2139.96 | -5.3% | $-1139.96 | -3.5 | done | losing for real |
| always_up | 4076 | 47.4 | 49.5 | $-3589.23 | -8.8% | $-2589.23 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6480 | 48.3 | 49.1 | $-3482.31 |
| ETH | 7064 | 48.1 | 48.5 | $-4366.94 |
| SOL | 7425 | 48.2 | 48.6 | $-4191.68 |
| XRP | 7456 | 48.2 | 48.4 | $-4643.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
