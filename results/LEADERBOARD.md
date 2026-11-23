# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 1:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1175 windows, 32488 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 627 | 34.9 | 35.3 | $-345.19 | -5.5% | $654.81 | -1.0 | done | can't tell from luck |
| value_ev10 | 1536 | 38.5 | 39.2 | $-791.76 | -5.2% | $208.24 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3258 | 50.9 | 50.4 | $-1000.39 | -3.1% | $-0.39 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2742 | 49.6 | 49.4 | $-1196.21 | -4.4% | $-196.21 | -2.3 | done | losing for real |
| value_ev5 | 2326 | 40.3 | 41.1 | $-1250.47 | -5.4% | $-250.47 | -2.2 | done | losing for real |
| trend_filter | 1923 | 48.9 | 50.4 | $-1559.13 | -8.1% | $-559.13 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2742 | 50.4 | 51.1 | $-1697.83 | -6.2% | $-697.83 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3258 | 49.1 | 50.2 | $-2014.99 | -6.2% | $-1014.99 | -3.6 | done | losing for real |
| coinflip | 4692 | 50.1 | 50.2 | $-2105.61 | -4.5% | $-1105.61 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4692 | 50.1 | 51.4 | $-2991.17 | -6.4% | $-1991.17 | -4.5 | done | losing for real |
| always_up | 4692 | 47.8 | 49.3 | $-3405.43 | -7.3% | $-2405.43 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7457 | 48.2 | 49.0 | $-3972.18 |
| ETH | 8060 | 48.1 | 48.4 | $-4828.27 |
| SOL | 8448 | 48.1 | 48.4 | $-4511.40 |
| XRP | 8523 | 48.1 | 48.2 | $-5046.34 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
