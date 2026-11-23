# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 12:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1171 windows, 32378 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 623 | 35.0 | 35.3 | $-341.04 | -5.5% | $658.96 | -1.0 | done | can't tell from luck |
| value_ev10 | 1531 | 38.5 | 39.2 | $-802.45 | -5.2% | $197.55 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3246 | 50.8 | 50.4 | $-1054.68 | -3.2% | $-54.68 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2733 | 49.7 | 49.4 | $-1182.85 | -4.3% | $-182.85 | -2.3 | done | losing for real |
| value_ev5 | 2318 | 40.3 | 41.1 | $-1248.93 | -5.4% | $-248.93 | -2.2 | done | losing for real |
| trend_filter | 1920 | 49.0 | 50.5 | $-1529.13 | -8.0% | $-529.13 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2733 | 50.3 | 51.1 | $-1688.51 | -6.2% | $-688.51 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3246 | 49.2 | 50.2 | $-1961.41 | -6.0% | $-961.41 | -3.5 | done | losing for real |
| coinflip | 4676 | 50.1 | 50.2 | $-2052.88 | -4.4% | $-1052.88 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 4676 | 50.2 | 51.4 | $-2872.66 | -6.1% | $-1872.66 | -4.3 | done | losing for real |
| always_up | 4676 | 47.8 | 49.3 | $-3398.89 | -7.3% | $-2398.89 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7430 | 48.3 | 49.0 | $-3874.84 |
| ETH | 8033 | 48.1 | 48.4 | $-4729.34 |
| SOL | 8420 | 48.1 | 48.4 | $-4472.76 |
| XRP | 8495 | 48.1 | 48.2 | $-5056.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
