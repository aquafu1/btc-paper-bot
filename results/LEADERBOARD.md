# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 7:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 478 windows, 13123 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 239 | 35.1 | 35.9 | $-135.26 | -5.7% | $864.74 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1111 | 50.9 | 50.0 | $-279.63 | -2.5% | $720.37 | -0.8 | done | can't tell from luck |
| value_ev10 | 618 | 39.0 | 40.2 | $-384.93 | -6.2% | $615.07 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1326 | 50.0 | 50.0 | $-474.47 | -3.6% | $525.53 | -1.3 | done | can't tell from luck |
| trend_filter | 766 | 49.6 | 50.8 | $-483.78 | -6.3% | $516.22 | -1.8 | done | can't tell from luck |
| value_ev5 | 914 | 40.9 | 41.9 | $-537.62 | -5.9% | $462.38 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1326 | 50.0 | 51.5 | $-906.32 | -6.8% | $93.68 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1111 | 49.1 | 51.5 | $-969.39 | -8.7% | $30.61 | -3.0 | done | losing for real |
| coinflip | 1904 | 49.9 | 50.8 | $-1062.32 | -5.6% | $-62.32 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 1904 | 49.7 | 51.7 | $-1375.10 | -7.2% | $-375.10 | -3.3 | done | losing for real |
| always_up | 1904 | 46.5 | 50.4 | $-2183.96 | -11.5% | $-1183.96 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2964 | 47.4 | 49.3 | $-2319.25 |
| ETH | 3290 | 48.1 | 48.9 | $-2183.87 |
| SOL | 3414 | 47.7 | 49.3 | $-2521.91 |
| XRP | 3455 | 48.6 | 49.1 | $-1767.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
