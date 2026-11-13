# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 13, 4:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 274 windows, 7196 settled trades, 72 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_15m_0.10pct | 707 | 54.7 | 52.3 | $+50.11 | +0.7% | $1050.11 | +0.2 | done | can't tell from luck |
| value_ev20 | 129 | 35.7 | 37.0 | $-108.42 | -8.4% | $891.58 | -0.7 | Sun 8:30 AM | too few trades (129/200) |
| reversal_60m_0.30pct | 577 | 52.0 | 52.3 | $-272.99 | -4.7% | $727.01 | -1.2 | done | can't tell from luck |
| value_ev10 | 347 | 38.3 | 40.8 | $-342.93 | -9.9% | $657.07 | -1.6 | done | can't tell from luck |
| trend_filter | 378 | 47.1 | 50.1 | $-400.31 | -10.6% | $599.69 | -2.1 | done | losing for real |
| value_ev5 | 510 | 40.4 | 42.4 | $-456.80 | -9.0% | $543.20 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 577 | 48.0 | 49.6 | $-466.48 | -8.1% | $533.52 | -2.0 | done | can't tell from luck |
| coinflip | 1088 | 49.7 | 50.9 | $-711.01 | -6.5% | $288.99 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1088 | 49.9 | 51.4 | $-763.21 | -7.0% | $236.79 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 707 | 45.3 | 49.6 | $-902.66 | -12.8% | $97.34 | -3.4 | done | losing for real |
| always_up | 1088 | 47.0 | 50.3 | $-1168.89 | -10.7% | $-168.89 | -3.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1607 | 46.7 | 49.5 | $-1644.10 |
| ETH | 1796 | 46.9 | 49.0 | $-1749.58 |
| SOL | 1862 | 48.5 | 49.3 | $-1309.53 |
| XRP | 1931 | 49.0 | 49.1 | $-840.39 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
