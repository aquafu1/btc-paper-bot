# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 1:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1174 windows, 32461 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 627 | 34.9 | 35.3 | $-345.19 | -5.5% | $654.81 | -1.0 | done | can't tell from luck |
| value_ev10 | 1536 | 38.5 | 39.2 | $-791.76 | -5.2% | $208.24 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3254 | 50.8 | 50.4 | $-1037.50 | -3.2% | $-37.50 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2739 | 49.6 | 49.4 | $-1204.20 | -4.4% | $-204.20 | -2.3 | done | losing for real |
| value_ev5 | 2326 | 40.3 | 41.1 | $-1250.47 | -5.4% | $-250.47 | -2.2 | done | losing for real |
| trend_filter | 1922 | 48.9 | 50.5 | $-1549.13 | -8.1% | $-549.13 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2739 | 50.4 | 51.1 | $-1686.22 | -6.2% | $-686.22 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3254 | 49.2 | 50.2 | $-1974.99 | -6.1% | $-974.99 | -3.5 | done | losing for real |
| coinflip | 4688 | 50.0 | 50.2 | $-2142.71 | -4.6% | $-1142.71 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4688 | 50.1 | 51.4 | $-2951.17 | -6.3% | $-1951.17 | -4.4 | done | losing for real |
| always_up | 4688 | 47.9 | 49.3 | $-3365.43 | -7.2% | $-2365.43 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7450 | 48.2 | 49.0 | $-3961.84 |
| ETH | 8055 | 48.1 | 48.4 | $-4819.72 |
| SOL | 8440 | 48.1 | 48.4 | $-4486.56 |
| XRP | 8516 | 48.1 | 48.2 | $-5030.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
