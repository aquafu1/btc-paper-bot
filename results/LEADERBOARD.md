# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 12:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 451 windows, 12387 settled trades, 38 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 227 | 34.8 | 36.0 | $-152.39 | -6.7% | $847.61 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1051 | 51.3 | 50.0 | $-189.67 | -1.8% | $810.33 | -0.6 | done | can't tell from luck |
| trend_filter | 713 | 50.1 | 50.7 | $-377.75 | -5.3% | $622.25 | -1.4 | done | can't tell from luck |
| value_ev10 | 585 | 38.8 | 40.1 | $-391.01 | -6.7% | $608.99 | -1.3 | done | can't tell from luck |
| value_ev5 | 866 | 41.0 | 41.8 | $-495.69 | -5.7% | $504.31 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1250 | 49.7 | 50.0 | $-534.54 | -4.3% | $465.46 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1250 | 50.3 | 51.6 | $-849.50 | -6.8% | $150.50 | -2.5 | done | losing for real |
| coinflip | 1798 | 49.8 | 50.8 | $-1040.66 | -5.8% | $-40.66 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1051 | 48.7 | 51.7 | $-1059.31 | -10.1% | $-59.31 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1798 | 49.6 | 51.5 | $-1302.97 | -7.2% | $-302.97 | -3.2 | done | losing for real |
| always_up | 1798 | 45.8 | 50.6 | $-2382.60 | -13.3% | $-1382.60 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2800 | 47.5 | 49.3 | $-2252.29 |
| ETH | 3110 | 47.9 | 48.8 | $-2100.86 |
| SOL | 3218 | 47.6 | 49.3 | $-2520.33 |
| XRP | 3259 | 48.4 | 49.2 | $-1902.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
