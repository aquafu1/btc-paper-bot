# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1276 windows, 34288 settled trades, 389 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 671 | 34.1 | 35.3 | $-520.36 | -7.8% | $479.64 | -1.5 | done | can't tell from luck |
| value_ev10 | 1645 | 38.6 | 39.2 | $-833.77 | -5.1% | $166.23 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3438 | 50.7 | 50.2 | $-1183.73 | -3.4% | $-183.73 | -2.0 | done | losing for real |
| value_ev5 | 2487 | 40.5 | 41.1 | $-1275.12 | -5.1% | $-275.12 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2873 | 49.5 | 49.4 | $-1328.28 | -4.6% | $-328.28 | -2.5 | done | losing for real |
| trend_filter | 2031 | 49.0 | 50.4 | $-1628.58 | -8.0% | $-628.58 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2873 | 50.5 | 51.0 | $-1652.79 | -5.8% | $-652.79 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3438 | 49.3 | 50.2 | $-2043.03 | -5.9% | $-1043.03 | -3.5 | done | losing for real |
| coinflip | 4944 | 49.9 | 50.1 | $-2289.18 | -4.6% | $-1289.18 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 4944 | 50.4 | 51.4 | $-2805.28 | -5.7% | $-1805.28 | -4.1 | done | losing for real |
| always_up | 4944 | 47.8 | 49.4 | $-3654.84 | -7.4% | $-2654.84 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8163 | 48.0 | 48.9 | $-4837.06 |
| ETH | 8815 | 48.2 | 48.3 | $-4793.66 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
