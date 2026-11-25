# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 5:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1429 windows, 36519 settled trades, 441 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 735 | 34.6 | 35.3 | $-515.63 | -7.0% | $484.37 | -1.5 | done | can't tell from luck |
| value_ev10 | 1774 | 38.8 | 39.1 | $-813.63 | -4.6% | $186.37 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3646 | 50.9 | 50.1 | $-983.46 | -2.7% | $16.54 | -1.6 | done | can't tell from luck |
| value_ev5 | 2676 | 40.5 | 41.1 | $-1298.07 | -4.9% | $-298.07 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3062 | 49.2 | 49.3 | $-1528.56 | -5.0% | $-528.56 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3062 | 50.8 | 51.0 | $-1548.70 | -5.1% | $-548.70 | -2.9 | done | losing for real |
| trend_filter | 2168 | 48.6 | 50.3 | $-1878.27 | -8.7% | $-878.27 | -4.1 | done | losing for real |
| coinflip | 5250 | 50.1 | 50.0 | $-2209.29 | -4.2% | $-1209.29 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3646 | 49.1 | 50.2 | $-2265.49 | -6.2% | $-1265.49 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5250 | 50.2 | 51.4 | $-3221.88 | -6.1% | $-2221.88 | -4.6 | done | losing for real |
| always_up | 5250 | 47.9 | 49.2 | $-3616.05 | -6.9% | $-2616.05 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9259 | 48.1 | 48.7 | $-4921.27 |
| ETH | 9950 | 48.0 | 48.0 | $-5373.52 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
