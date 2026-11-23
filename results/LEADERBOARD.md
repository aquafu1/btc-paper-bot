# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 2:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1178 windows, 32551 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 629 | 34.8 | 35.3 | $-365.19 | -5.8% | $634.81 | -1.1 | done | can't tell from luck |
| value_ev10 | 1539 | 38.5 | 39.2 | $-802.98 | -5.2% | $197.02 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3263 | 50.8 | 50.4 | $-1050.39 | -3.2% | $-50.39 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2744 | 49.6 | 49.4 | $-1200.88 | -4.4% | $-200.88 | -2.3 | done | losing for real |
| value_ev5 | 2332 | 40.2 | 41.1 | $-1291.69 | -5.5% | $-291.69 | -2.3 | done | losing for real |
| trend_filter | 1925 | 48.9 | 50.5 | $-1546.43 | -8.0% | $-546.43 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2744 | 50.4 | 51.1 | $-1698.32 | -6.2% | $-698.32 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3263 | 49.2 | 50.2 | $-1975.04 | -6.1% | $-975.04 | -3.5 | done | losing for real |
| coinflip | 4704 | 50.0 | 50.2 | $-2154.87 | -4.6% | $-1154.87 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4704 | 50.1 | 51.4 | $-2957.99 | -6.3% | $-1957.99 | -4.4 | done | losing for real |
| always_up | 4704 | 47.8 | 49.3 | $-3492.31 | -7.4% | $-2492.31 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7467 | 48.2 | 49.0 | $-4012.35 |
| ETH | 8072 | 48.1 | 48.4 | $-4874.74 |
| SOL | 8466 | 48.1 | 48.4 | $-4541.22 |
| XRP | 8546 | 48.1 | 48.2 | $-5107.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
