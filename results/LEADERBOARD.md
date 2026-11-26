# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 3:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1519 windows, 37656 settled trades, 365 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 765 | 34.6 | 35.4 | $-536.35 | -7.0% | $463.65 | -1.5 | done | can't tell from luck |
| value_ev10 | 1842 | 38.7 | 39.2 | $-921.56 | -5.0% | $78.44 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3742 | 50.9 | 50.1 | $-961.31 | -2.6% | $38.69 | -1.6 | done | can't tell from luck |
| value_ev5 | 2778 | 40.6 | 41.1 | $-1326.18 | -4.8% | $-326.18 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3138 | 51.1 | 51.0 | $-1426.82 | -4.5% | $-426.82 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3138 | 48.9 | 49.2 | $-1716.88 | -5.5% | $-716.88 | -3.0 | done | losing for real |
| trend_filter | 2227 | 48.5 | 50.3 | $-1922.55 | -8.6% | $-922.55 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3742 | 49.1 | 50.2 | $-2313.97 | -6.2% | $-1313.97 | -3.8 | done | losing for real |
| coinflip | 5428 | 50.0 | 50.0 | $-2390.69 | -4.4% | $-1390.69 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5428 | 50.1 | 51.3 | $-3354.58 | -6.2% | $-2354.58 | -4.7 | done | losing for real |
| always_up | 5428 | 48.1 | 49.2 | $-3499.10 | -6.4% | $-2499.10 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9798 | 48.0 | 48.7 | $-5397.06 |
| ETH | 10548 | 48.1 | 47.9 | $-5388.72 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
