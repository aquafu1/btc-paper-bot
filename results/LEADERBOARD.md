# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 2:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1033 windows, 28718 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 533 | 34.7 | 35.1 | $-283.54 | -5.3% | $716.46 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2923 | 51.2 | 50.5 | $-841.68 | -2.9% | $158.32 | -1.6 | done | can't tell from luck |
| value_ev10 | 1323 | 37.5 | 39.2 | $-985.09 | -7.4% | $14.91 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2462 | 49.8 | 49.6 | $-1092.65 | -4.4% | $-92.65 | -2.2 | done | losing for real |
| trend_filter | 1718 | 49.4 | 50.7 | $-1311.06 | -7.6% | $-311.06 | -3.2 | done | losing for real |
| value_ev5 | 2002 | 39.5 | 41.0 | $-1404.40 | -7.0% | $-404.40 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2462 | 50.2 | 51.0 | $-1631.08 | -6.6% | $-631.08 | -3.4 | done | losing for real |
| coinflip | 4124 | 50.5 | 50.3 | $-1661.50 | -4.0% | $-661.50 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2923 | 48.8 | 50.2 | $-1998.29 | -6.8% | $-998.29 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4124 | 50.7 | 51.5 | $-2249.18 | -5.5% | $-1249.18 | -3.6 | done | losing for real |
| always_up | 4124 | 47.4 | 49.5 | $-3570.08 | -8.7% | $-2570.08 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6548 | 48.3 | 49.1 | $-3595.09 |
| ETH | 7126 | 48.1 | 48.5 | $-4397.44 |
| SOL | 7495 | 48.2 | 48.6 | $-4300.41 |
| XRP | 7549 | 48.1 | 48.3 | $-4735.63 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
