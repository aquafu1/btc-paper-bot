# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1251 windows, 33930 settled trades, 401 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 665 | 34.1 | 35.3 | $-524.16 | -7.9% | $475.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1626 | 38.4 | 39.2 | $-900.17 | -5.5% | $99.83 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3401 | 50.8 | 50.3 | $-1122.03 | -3.3% | $-122.03 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2845 | 49.5 | 49.4 | $-1299.58 | -4.6% | $-299.58 | -2.4 | done | losing for real |
| value_ev5 | 2457 | 40.3 | 41.1 | $-1348.76 | -5.5% | $-348.76 | -2.3 | done | losing for real |
| trend_filter | 2008 | 48.8 | 50.4 | $-1677.72 | -8.4% | $-677.72 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2845 | 50.5 | 51.1 | $-1693.74 | -6.0% | $-693.74 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3401 | 49.2 | 50.2 | $-2097.63 | -6.2% | $-1097.63 | -3.6 | done | losing for real |
| coinflip | 4894 | 50.0 | 50.1 | $-2218.00 | -4.5% | $-1218.00 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4894 | 50.3 | 51.4 | $-2905.32 | -5.9% | $-1905.32 | -4.3 | done | losing for real |
| always_up | 4894 | 47.8 | 49.3 | $-3647.12 | -7.5% | $-2647.12 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7993 | 48.0 | 48.9 | $-4791.03 |
| ETH | 8627 | 48.1 | 48.3 | $-5058.96 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
