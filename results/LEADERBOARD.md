# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 5:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1622 windows, 39021 settled trades, 343 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 825 | 34.3 | 35.2 | $-634.04 | -7.7% | $365.96 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3847 | 50.8 | 50.0 | $-1014.52 | -2.6% | $-14.52 | -1.6 | done | can't tell from luck |
| value_ev10 | 1953 | 38.3 | 39.0 | $-1117.37 | -5.7% | $-117.37 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3218 | 51.1 | 50.9 | $-1475.66 | -4.6% | $-475.66 | -2.7 | done | losing for real |
| value_ev5 | 2921 | 40.4 | 41.0 | $-1547.78 | -5.3% | $-547.78 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3218 | 48.9 | 49.2 | $-1751.56 | -5.4% | $-751.56 | -3.1 | done | losing for real |
| trend_filter | 2287 | 48.4 | 50.4 | $-2058.85 | -9.0% | $-1058.85 | -4.4 | done | losing for real |
| coinflip | 5635 | 50.1 | 49.9 | $-2305.55 | -4.1% | $-1305.55 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3847 | 49.2 | 50.2 | $-2358.31 | -6.1% | $-1358.31 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5635 | 50.2 | 51.3 | $-3494.63 | -6.2% | $-2494.63 | -4.8 | done | losing for real |
| always_up | 5635 | 48.1 | 49.1 | $-3647.06 | -6.5% | $-2647.06 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10418 | 47.9 | 48.6 | $-5940.84 |
| ETH | 11293 | 48.0 | 47.7 | $-5880.27 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
