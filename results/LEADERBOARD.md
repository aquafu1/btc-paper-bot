# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 5:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1524 windows, 37719 settled trades, 375 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 766 | 34.6 | 35.4 | $-546.35 | -7.1% | $453.65 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3748 | 51.0 | 50.0 | $-940.98 | -2.5% | $59.02 | -1.5 | done | can't tell from luck |
| value_ev10 | 1844 | 38.6 | 39.2 | $-941.56 | -5.1% | $58.44 | -1.8 | done | can't tell from luck |
| value_ev5 | 2783 | 40.6 | 41.1 | $-1350.68 | -4.9% | $-350.68 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3142 | 51.1 | 51.0 | $-1403.77 | -4.5% | $-403.77 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3142 | 48.9 | 49.2 | $-1740.47 | -5.5% | $-740.47 | -3.1 | done | losing for real |
| trend_filter | 2232 | 48.5 | 50.3 | $-1956.14 | -8.8% | $-956.14 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3748 | 49.0 | 50.2 | $-2349.40 | -6.3% | $-1349.40 | -3.9 | done | losing for real |
| coinflip | 5438 | 50.0 | 50.0 | $-2371.29 | -4.4% | $-1371.29 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5438 | 50.1 | 51.3 | $-3395.18 | -6.2% | $-2395.18 | -4.7 | done | losing for real |
| always_up | 5438 | 48.1 | 49.1 | $-3517.63 | -6.5% | $-2517.63 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9828 | 48.0 | 48.7 | $-5473.53 |
| ETH | 10581 | 48.1 | 47.9 | $-5455.71 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
