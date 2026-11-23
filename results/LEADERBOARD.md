# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 11:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1213 windows, 33361 settled trades, 282 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 652 | 34.5 | 35.3 | $-443.45 | -6.8% | $556.55 | -1.3 | done | can't tell from luck |
| value_ev10 | 1596 | 38.7 | 39.2 | $-781.50 | -4.9% | $218.50 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3343 | 50.8 | 50.3 | $-1073.68 | -3.2% | $-73.68 | -1.9 | done | can't tell from luck |
| value_ev5 | 2413 | 40.5 | 41.1 | $-1209.84 | -5.0% | $-209.84 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2797 | 49.5 | 49.4 | $-1292.88 | -4.6% | $-292.88 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2797 | 50.5 | 51.1 | $-1639.23 | -5.9% | $-639.23 | -3.2 | done | losing for real |
| trend_filter | 1972 | 48.7 | 50.4 | $-1682.81 | -8.5% | $-682.81 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3343 | 49.2 | 50.2 | $-2063.21 | -6.2% | $-1063.21 | -3.6 | done | losing for real |
| coinflip | 4816 | 50.0 | 50.1 | $-2208.13 | -4.6% | $-1208.13 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4816 | 50.2 | 51.4 | $-2916.16 | -6.1% | $-1916.16 | -4.3 | done | losing for real |
| always_up | 4816 | 47.9 | 49.3 | $-3488.75 | -7.2% | $-2488.75 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7714 | 48.1 | 48.9 | $-4295.05 |
| ETH | 8337 | 48.1 | 48.3 | $-4920.35 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
