# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 973 windows, 27016 settled trades, 37 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 496 | 34.7 | 34.8 | $-219.50 | -4.4% | $780.50 | -0.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2760 | 51.2 | 50.5 | $-752.36 | -2.7% | $247.64 | -1.4 | done | can't tell from luck |
| value_ev10 | 1232 | 37.8 | 39.1 | $-774.80 | -6.3% | $225.20 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2310 | 50.2 | 49.7 | $-876.42 | -3.8% | $123.58 | -1.8 | done | can't tell from luck |
| value_ev5 | 1869 | 39.8 | 41.0 | $-1113.54 | -6.0% | $-113.54 | -2.2 | done | losing for real |
| trend_filter | 1618 | 49.8 | 50.9 | $-1143.34 | -7.1% | $-143.34 | -2.9 | done | losing for real |
| reversal_60m_0.30pct | 2310 | 49.8 | 50.9 | $-1671.35 | -7.2% | $-671.35 | -3.6 | done | losing for real |
| coinflip | 3887 | 50.2 | 50.3 | $-1798.03 | -4.6% | $-798.03 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2760 | 48.8 | 50.3 | $-1952.56 | -7.1% | $-952.56 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 3887 | 50.7 | 51.5 | $-2155.17 | -5.5% | $-1155.17 | -3.6 | done | losing for real |
| always_up | 3887 | 46.8 | 49.6 | $-3871.49 | -10.0% | $-2871.49 | -6.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6150 | 48.1 | 49.1 | $-3566.01 |
| ETH | 6717 | 48.0 | 48.5 | $-4347.56 |
| SOL | 7057 | 48.2 | 48.6 | $-4039.54 |
| XRP | 7092 | 48.1 | 48.4 | $-4375.44 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
