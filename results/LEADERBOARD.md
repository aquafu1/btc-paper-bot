# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 4:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 947 windows, 26265 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 485 | 35.3 | 34.8 | $-134.35 | -2.8% | $865.65 | -0.5 | done | can't tell from luck |
| value_ev10 | 1191 | 38.2 | 39.1 | $-625.13 | -5.2% | $374.87 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2684 | 51.1 | 50.6 | $-837.35 | -3.1% | $162.65 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 2248 | 50.2 | 49.7 | $-860.04 | -3.8% | $139.96 | -1.8 | done | can't tell from luck |
| trend_filter | 1566 | 50.1 | 50.9 | $-995.70 | -6.4% | $4.30 | -2.6 | done | losing for real |
| value_ev5 | 1810 | 39.9 | 41.0 | $-1008.91 | -5.6% | $-8.91 | -2.0 | done | can't tell from luck |
| coinflip | 3783 | 50.3 | 50.4 | $-1618.63 | -4.3% | $-618.63 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2248 | 49.8 | 51.0 | $-1624.77 | -7.2% | $-624.77 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 2684 | 48.9 | 50.2 | $-1775.06 | -6.6% | $-775.06 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3783 | 51.0 | 51.6 | $-1848.91 | -4.9% | $-848.91 | -3.1 | done | losing for real |
| always_up | 3783 | 46.9 | 49.6 | $-3723.32 | -9.8% | $-2723.32 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5983 | 48.2 | 49.0 | $-3428.01 |
| ETH | 6539 | 48.2 | 48.5 | $-3945.53 |
| SOL | 6846 | 48.3 | 48.6 | $-3750.41 |
| XRP | 6897 | 48.3 | 48.5 | $-3928.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
